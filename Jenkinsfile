pipeline {
  environment {
    registry = "iditg/hello-world"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    #stage('Clone Git') {
    #  steps {
    #    sh "git clone -b dev https://github.com/Iditgl/react-hello-world.git"
        #git 'https://github.com/Iditgl/react-hello-world.git'
    #  }
    #}
    stage('Start Docker Service') {
      steps {
        sh "sudo systemctl enable docker"
        sh "sudo systemctl start docker"
      }
    } 
    stage('Build image') {
      steps {
        script {
        //app = sh "sudo docker build -t ${env.registry}:latest ."
	app = sh "sudo docker build -t ${env.registry}:${BUILD_NUMBER} ."    
      }
    }
}
    stage('Publish Image') {
      steps {
         // sh "sudo docker push ${env.registry}:latest"
           sh "sudo docker push ${env.registry}:${BUILD_NUMBER}"
        }
      }
    
    stage('Deploy image to k8s') {
      steps {
           sh "sudo kubectl apply -f ./client-deployment.yaml"
        }
      } 
    //stage('Deploy image to k8s') { 
    //kubernetesDeploy(kubeconfigId: 'k8s_master',configs: 'my_proj_dep.yml',enableConfigSubstitution: true)
    //}
      }    
}
