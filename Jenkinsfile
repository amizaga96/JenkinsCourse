pipeline {
  agent { node { label 'slave02' } }

   stages {
      stage('Clone Sources') {
        steps {
          checkout scm
        } 
      }
      stage('Execute C exe file') {
         steps {
            echo 'Compilation process..'
            sh '''
            if [ "$LANGUISH" = "C" -o "$LANGUISH" = "All" ]; then
				echo "Put C code"
            else
				echo "Passing.. "$LANGUISH" is not C" 
			fi
            '''
             
         }
      }
      stage('Execute python script') {
         steps {
            echo 'Execute python script'
            sh '''
			if [ "$LANGUISH" = "Python" -o "$LANGUISH" = "All" ]; then
				chmod 755 ${WORKSPACE}/Python/login.py
				${WORKSPACE}/Python/login.py $FIRST_NAME $LAST_NAME
				echo 'Python script run successfully'
			else
				echo "Passing.. "$LANGUISH" is not Python"
			fi
            '''
            
         }
      }
      stage('Execute bash script') {
         steps {
			echo 'Execute bash script'
			sh '''
			if [ "$LANGUISH" = "Bash" -o "$LANGUISH" = "All" ]; then
				chmod 755 ${WORKSPACE}/Bash/login.sh
				${WORKSPACE}/Bash/login.sh $FIRST_NAME $LAST_NAME
				echo 'Bash script run successfully'
			else
				echo "Passing.. "$LANGUISH" is not Bash"
			fi
			'''
         }
      }
      
   }
}
