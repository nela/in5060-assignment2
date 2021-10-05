# IN5060 - Assignment2

# Members

* Nemanja Lakicevic
* Vemund Sjøvold Sundal

# Contents

* `mock_data` contains a script to create the mock data and the mock data
itself

# Usage

* `./mock_data/create-mock-data.sh` to run from the command line. This option specifies
no arguments and will only print the mock data results to console

  * `-o | --output` - Outputs script results to a new file. The file *must
  not exist before the script is executed* as it will exit in order to avoid
  overwriting existing file.
  * `-a | --append` - Appends script results to an existing file. The file *must
  exist before the script is executed* as it will exit in case the file is not
  found.
  * `-s | --seed` - Provides the seed to randomization and outputs
  deterministic results
  * If unknown options are provided the script will simply exit
