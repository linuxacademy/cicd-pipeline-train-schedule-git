pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
          echo 'Running build automation'
          sh './gradlew build --no-daemon'
          archiveArtifacts artifacts: 'dist/trainSchedule.zip'
      }
    }
    stage('DeployToStaging') {
      when {
          branch 'master'
      }
      steps {
        withCredentials([usernamePassword(credentialsId: 'staging-key', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
          sshPublisher(
            failOnError: true,
            continueOnError: false,
            publishers: [
              sshPublisherDesc(
                configName: '	staging-node',
                sshCredentials: [
                  username: "$USERNAME",
                  encryptedPassphrase: "$USERPASS"
                ], 
                transfers: [
                  sshTransfer(
                    sourceFiles: 'dist/trainSchedule.zip',
                    removePrefix: 'dist/',
                    remoteDirectory: '/tmp'
                  )
                ]
              )
            ]
          )
	}
      }
    }
    stage('DeployToProduction') {
      when {
        branch 'master'
      }
      steps {
        input 'Does the staging environment look OK?'
        milestone(1)
        withCredentials([usernamePassword(credentialsId: 'staging-key', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
          sshPublisher(
            failOnError: true,
            continueOnError: false,
            publishers: [
              sshPublisherDesc(
                configName: 'production-node',
                sshCredentials: [
                  username: "$USERNAME",
                  encryptedPassphrase: "$USERPASS"
                ], 
                transfers: [
                  sshTransfer(
                    sourceFiles: 'dist/trainSchedule.zip',
                    removePrefix: 'dist/',
                    remoteDirectory: '/tmp',
                    execCommand: 'sudo /usr/bin/systemctl stop train-schedule && rm -rf /opt/train-schedule/* && unzip /tmp/trainSchedule.zip -d /opt/train-schedule && sudo /usr/bin/systemctl start train-schedule'
                  )
                ]
              )
            ]
          )
        }
      }
    }
  }
}
