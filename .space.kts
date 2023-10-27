import java.time.LocalDate

job("Distribute Python Consumer Package") {

	startOn {
        gitPush {
            anyBranchMatching {
                +"release/*"
                +"master"
                +"main"
            }
        }
    }

	parameters {
      text("EAPP_PYTHON_CONSUMER_DIR", value = "/mnt/space/work/eapp-python-consumer")
    }


    container(displayName = "Setup Version", image = "amazoncorretto:17-alpine") {
        kotlinScript { api ->
            // Get the current year and month
            val currentYear = (LocalDate.now().year % 100).toString().padStart(2, '0')
            val currentMonth = LocalDate.now().monthValue.toString()

            // Get the execution number from environment variables
            val currentExecution = System.getenv("JB_SPACE_EXECUTION_NUMBER")

            // Set the VERSION_NUMBER parameter
            api.parameters["VERSION_NUMBER"] = "$currentYear.$currentMonth.$currentExecution"
        }
    }

    container(displayName = "Python Consumer Build", image = "python:3.9.16") {

        env["EAPP_PYTHON_CONSUMER_DIR"] = "{{ EAPP_PYTHON_CONSUMER_DIR }}"

        shellScript {
          content = """

            echo "Ensure you can run pip from the command line"
            python3 -m pip --version
            python3 -m ensurepip --default-pip

            echo "Ensure pip, setuptools, and wheel are up to date"
            python3 -m pip install --upgrade pip setuptools wheel

            echo "Install required packages for python build"
            python3 -m pip install twine==4.0.1

            echo "Configure pypirc"
            cp ${'$'}EAPP_PYTHON_CONSUMER_DIR/pypirc ~/.pypirc

            sed "10s/.*/    version='{{ VERSION_NUMBER }}',/" ${'$'}EAPP_PYTHON_CONSUMER_DIR/setup.py > ${'$'}EAPP_PYTHON_CONSUMER_DIR/newsetup.py
            mv ${'$'}EAPP_PYTHON_CONSUMER_DIR/newsetup.py ${'$'}EAPP_PYTHON_CONSUMER_DIR/setup.py

            echo "Build Package"
            python3 setup.py sdist

            echo "Inspect Package"
            tar -tvf ${'$'}EAPP_PYTHON_CONSUMER_DIR/dist/eapp_python_consumer-{{ VERSION_NUMBER }}.tar.gz

            echo "Publish Package"
            twine upload -r local dist/*

          """
        }
    }
}