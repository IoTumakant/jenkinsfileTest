pipeline {
	agent {
		 node {
			label 'Window_agent'
		}
	}

    stages {
	 stage('Build') {
		 steps {

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
