pipeline {
	
	
	agent {
		 node {
			label 'MasterNode'
		}
	}

    stages {
	 stage('Build Docker Image form Docker file') {
		 steps {
			echo 'Building Docker Image'
			script {
				sh 'sudo docker build -t umakant123iot/timelog_py_app -f Dockerfile .'
			}
	            }
	}	
        stage('Docker Hub login and push image') {
                 steps {
                        echo 'Pushing Image to Docker Hub'
                        script {
                                withCredentials([string(credentialsId: 'Docker_Hub_Pass', variable: 'Docker_Hub_Pass')]) {
					sh 'sudo docker login -u umakant123iot -p ${Docker_Hub_Pass}'
				}
				sh 'sudo docker push umakant123iot/timelog_py_app'
                        }
                    }
        }
	 stage('Application deployment as Docker container on Deployment server') {
                 steps {
                        echo 'Deploying Application'
                        script {
					sh 'chown jenkins linux123.pem'
					sh 'chmod 400 linux123.pem'
					sh'ssh -o StrictHostKeyChecking=no -i linux123.pem ubuntu@65.0.55.75 docker rm -f timelog_file || true'
					sh 'ssh -o StrictHostKeyChecking=no -i linux123.pem ubuntu@65.0.55.75 docker run -d --name timelog_file umakant123iot/timelog_py_app' 
                        }
                    }
        }

	stage('Test') {
            steps {
                echo 'Testing..'
		script {
                    sh 'python TimeLog_file.py'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
