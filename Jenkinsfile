pipeline {
  agent centOS
  stages{
    stage ('Build') {
      steps {
       echo 'Running build automation'
       sh  'mvn build'
       archiveArtifacts artifacts: 'dist/trainSchedule.zip'
       }
       }
       }
       }
