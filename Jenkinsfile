pipeline {
  environment {
    registry = "iditg/hello-world"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Clone Git') {
      steps {
        //sh "git clone -b dev https://github.com/Iditgl/react-hello-world.git"
        //git 'https://github.com/Iditgl/react-hello-world.git'
        git 'https://github.com/Iditgl/hello-react.git'
      }
    }
    stage('Start Docker Service') {
      steps {
        sh "sudo systemctl enable docker"
        sh "sudo systemctl start docker"
      }
    } 
    stage('Build image') {
      steps {
        script {
	app = sh "sudo docker build -t ${env.registry}:${BUILD_NUMBER} -t ${env.registry}:latest ."    
      }
    }
}
    stage('Publish Image') {
      steps {
           sh "sudo docker push ${env.registry}:latest"
           sh "sudo docker push ${env.registry}:${BUILD_NUMBER}"
        }
      }
    
    stage('Deploy image to k8s') {
      steps {
           //sh "sudo kubectl apply -f ./client-deployment.yaml"
            sh "sudo kubectl apply -f ./deployment.yaml"
            sh "sudo kubectl apply -f ./lb.yaml"
            sh "chmod +x lb.py"
            sh "./lb.py"
        }
      } 
    //stage('Deploy image to k8s') { 
    //kubernetesDeploy(kubeconfigId: 'k8s_master',configs: 'my_proj_dep.yml',enableConfigSubstitution: true)
    //}
      }    
}
