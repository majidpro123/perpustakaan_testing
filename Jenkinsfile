pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\majid\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
 // ganti sesuai path Python di mesin
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/majidpro123/perpustakaan_testing.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Menyiapkan environment Python...'
                bat """
                    %PYTHON% -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Menjalankan pytest...'
                bat """
                    call venv\\Scripts\\activate
                    pytest --junitxml=report.xml
                """
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Semua unit test berhasil!'
        }
        failure {
            echo '❌ Ada test yang gagal!'
        }
    }
}
