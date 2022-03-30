pipeline {
	agent {
		 node {
			label 'Window_agent'
		}
	}

    stages {
        stage('Git Clone') {
            steps {
                git 'https://github.com/IoTumakant/jenkinsfileTest.git' , branch: 'master'

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
