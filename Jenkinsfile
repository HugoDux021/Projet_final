pipeline {

      environment {
        PATH = "/var/jenkins_home/.local/bin:${env.PATH}"
        imagename = 'imagejenkins2'
        //registry = "formation2/projet"
        //registryCredential = 'dockerhub'
        //registryCredential = 'docker'
        } 

      agent any
      stages {
        stage('Clone sources') {
            steps {
                git url: 'https://github.com/HugoDux021/Projet_final.git',
                branch: "main"
            }
        }
        stage('continuous integration') { // Compile and do unit testing
             tools {
               gradle 'gradle'
            }
             steps {
                 parallel (
                 // run Gradle to execute compile and unit testing
                    pylint: {
                        sh 'gradle lint'
                    },
                    pycode: {
                        sh 'gradle pycode'
                    }
                )
             }
           }

        // stage('testcode') {
             // tools {
             //   gradle 'radle'
            // }
        //     steps {
        //         sh 'gradle test'
        //     }
        // }

        stage('Package and deploy') {
             tools {
               gradle 'gradle'
             }
            steps {
                sh 'gradle up'
            }
        }
      }
      post {
          always {
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'build', reportFiles: 'index.html', reportName: 'Flake 8 violations', reportTitles: ''])
            recordIssues(
                    tools: [pep8(pattern: 'gradle/result-pycode.report')]
                )
            //junit 'gradle/report_test.xml'
          }
      }
 }
