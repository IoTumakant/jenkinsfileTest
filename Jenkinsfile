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
                                sh 'docker login -u umakant123iot -p 123uk_aecs'
				sh 'sudo docker push umakant123iot/timelog_py_app'
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
