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
				cd  ${WORKSPACE}/Python
				chmod 755 pythonscript.py
				python pythonscript.py $NAME
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
				cd ${WORKSPACE}/Bash/
				chmod 755 bashscript.py
				bash bashscript.py $NAME
				echo 'Bash script run successfully'
			else
				echo "Passing.. "$LANGUISH" is not Bash"
			fi
			'''
         }
      }
      
   }
}
