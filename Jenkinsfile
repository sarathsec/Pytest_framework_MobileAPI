pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile tests/combo.py'
                stash(name: 'compiled-results', includes: 'tests/*.py*')
            }
        }
        stage('Test') { 
            steps {
                sh 'python combo.py regression,bvt,sanity GetAllTMU,GetAllDCU,GetAllMeter,GetAllRegion,GetAllSection' 
            }
        }
    }
}
