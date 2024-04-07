pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python All_services.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}