pipeline {
    environment {
        registry = "alinagomeniuc/docker-test"
        registryCredential = 'dockerhub'
        dockerImage = ''
  }

    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build -t test_jenkins:${BUILD_NUMBER} .'
                sh 'docker tag test_jenkins:${BUILD_NUMBER} test_jenkins:latest'
                sh 'docker run -d -i --name test_jenk --rm test_jenkins'
            }
        }

        stage('test') {
            steps {
                sh 'docker exec -i hg sh -c "pytest test_app.py"'
            }
        }

        stage('Publish') {
            steps {
            withDockerRegistry([ credentialsId: "6544de7e-17a4-4576-9b9b-e86bc1e4f903", url: "" ]) {
              sh 'docker push brightbox/terraform:latest'
            }
        }
    }

    post {
        always {
            sh 'docker rm -f test_jenk'
        }
    }
}