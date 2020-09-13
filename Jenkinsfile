pipeline {
    environment {
        registry = "alinagomeniuc/docker-test"
        registryCredential = 'test_dockerhub_jenkins'
        dockerImage = ''
  }

    agent any

    stages {
        stage('build') {
            steps {
                    script {
                        dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    }
            }
//             steps {
//                 sh 'docker build -t test_jenkins:${BUILD_NUMBER} .'
//                 sh 'docker tag test_jenkins:${BUILD_NUMBER} test_jenkins:latest'
//                 sh 'docker run -d -i --name test_jenk --rm test_jenkins'
//             }
        }

//         stage('test') {
//             steps {
//                 sh 'docker exec -i test_jenk sh -c "pytest test_app.py"'
//             }
//         }

//         stage('Publish') {
//             steps {
//             withDockerRegistry([ credentialsId: "6544de7e-17a4-4576-9b9b-e86bc1e4f903", url: "" ]) {
//               sh 'docker push brightbox/terraform:latest'
//             }
//         }

        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        always {
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
    }
}