#Source this script to setup the paths to use the toolkit!

#Folder of the script (not where it was sourced from)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PATH=$PATH:$DIR/sixtrack:$DIR/sixtrack/impacts_real
export PYTHONPATH=$PYTHONPATH:$DIR

export PATH=$PATH:$DIR/final_runscripts
