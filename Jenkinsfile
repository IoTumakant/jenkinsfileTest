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
				sh 'docker build -t umakant123iot/timelog_py_app -f Dockerfile .'
			}
	            }
	}	
        stage('Docker Hub login and push image') {
                 steps {
                        echo 'Pushing Image to Docker Hub'
                        script {
                                withCredentials([string(credentialsId: 'Docker_Hub_Pass', variable: 'Docker_Hub_Pass')]) {
					sh 'docker login -u umakant123iot -p ${Docker_Hub_Pass}'
				}
				sh 'docker push umakant123iot/timelog_py_app'
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
        stage('Deploy Application as Docker container on Deployment server') {
                 steps {
                        echo 'Deploying container from Docker hub image'
                        script {
				sshagent(['Docker_Dev_Server_SSH']) {
					sh 'ssh -o StrictHostKeyChecking=no ubuntu@15.206.81.223 docker rm -f timelogapp || true'
					sh 'ssh -o StrictHostKeyChecking=no ubuntu@15.206.81.223 docker run -d --name timelogapp umakant123iot/timelog_py_app'
				}
			}
		 }
	}

}
}
