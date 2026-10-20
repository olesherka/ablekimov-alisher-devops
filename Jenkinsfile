pipeline {
    agent any

    options {
        // the code is checked out in the Checkout stage below
        skipDefaultCheckout(true)
    }

    environment {
        STUDENT_NAME    = 'Alisher'
        STUDENT_SURNAME = 'Ablekimov'
        STUDENT_GROUP   = 'IT2-2312'
        STUDENT_ID      = '37637'
        IMAGE_NAME      = 'ablekimov-alisher-devops'
        CONTAINER_NAME  = 'ablekimov-alisher-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
                sh 'python3 -m py_compile app/app.py'
                sh 'bash -n scripts/Ablekimov_Alisher_system.sh'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
                sh 'grep "Student ID: 37637" Ablekimov_Alisher_info.txt'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER -t $IMAGE_NAME:latest .'
                sh 'docker images $IMAGE_NAME'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
                sh '''docker run -d --name $CONTAINER_NAME -p 5001:8080 \
                    -e STUDENT_NAME -e STUDENT_SURNAME -e STUDENT_GROUP -e STUDENT_ID \
                    $IMAGE_NAME:latest'''
                sh 'sleep 3'
                sh 'docker logs $CONTAINER_NAME'
                sh 'docker ps --filter name=$CONTAINER_NAME'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully'
        }
        failure {
            echo 'Pipeline failed, check the stage that is marked red'
        }
    }
}
