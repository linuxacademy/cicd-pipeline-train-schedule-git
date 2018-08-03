pipeline
{
  agent any									//to run on any agent
  stages{
    stage ('Build' ){
      steps {
        echo 'Running Build Automation'
        sh './gradlew build --no-daemon'
        archiveArtifacts artifacts: 'dist/trainSchedule.zip'
      }
    }
  }
}

