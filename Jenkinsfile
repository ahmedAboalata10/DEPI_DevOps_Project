
pipeline {
    agent any
    
    environment {
        dockerHubCredentialsID	    = 'DockerHub'  		    			// DockerHub credentials ID.
        imageName   		    = 'ahmedAboalata10/python-app'     			// DockerHub repo/image 

    }
     stages {
        stage('Build Docker Image') {
            steps {
                script {
                	// Navigate to the directory contains Dockerfile
                 	dir('app') {
                 		        echo "Building Docker image..."
                                sh "docker build -t ${imageName}:${BUILD_NUMBER} ."
                    	}
                }
            }
        }
        stage('push Docker Image') {
            steps {
                script {
                	// Navigate to the directory contains Dockerfile
                 	dir('app') {
                                withCredentials([usernamePassword(credentialsId: "${dockerHubCredentialsID}", usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                                sh "docker login -u ${USERNAME} -p ${PASSWORD}"
                        }
                        
                        // Build and push Docker image
                        echo "Pushing Docker image..."
                        sh "docker push ${imageName}:${BUILD_NUMBER}"
                    	}
                }
            }
        }


        stage('Deploy on EC2') {
            steps {
                script { 
            
				    sh "docker run -d -p 5000:5000 ${imageName}:${BUILD_NUMBER}"
                    
                }
            }
        }
    }

    post {
        success {
            echo "${JOB_NAME}-${BUILD_NUMBER} pipeline succeeded"
        }
        failure {
            echo "${JOB_NAME}-${BUILD_NUMBER} pipeline failed"
        }
    }
}