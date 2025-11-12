pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone repo dari GitHub
                git branch: 'main', url: 'https://github.com/majidpro120/perpustakaan_testing.git'
            }
        }

        stage('Setup Python') {
            steps {
                // Install Python dan dependencies
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest --maxfail=1 --disable-warnings -v
                '''
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml'
            echo 'Pipeline selesai dijalankan!'
        }
        success {
            echo '✅ Semua test lulus!'
        }
        failure {
            echo '❌ Ada test yang gagal!'
        }
    }
}
