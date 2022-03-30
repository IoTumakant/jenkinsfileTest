pipeline {
	
	
	agent {
		 node {
			def buildNumber = BUILD_NUMBER
			label 'MasterNode'
		}
	}

    stages {
	 stage('Build Docker Image form Docker file') {
		 steps {
			echo 'Building Docker Image'
			script {
				sh 'sudo docker build -t IoTumakant/timelog_py_app:${buildNumber} -f Dockerfile .'
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
