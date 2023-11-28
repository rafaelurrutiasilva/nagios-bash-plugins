# Nagios Plugins in Bash 
## Introduction
All plugins here are writen i bash script. They are tested in CentOS, Suse, RHEL and Photon OS.

## How to use
Use the argument ` --help ` to get infrmation about how to use the plugins here.

Script | Function
-------|---------
[check_by_top](https://github.com/rafaelurrutiasilva/nagios-bash-plugins/blob/main/plugins/check_by_top) | Will check tasks, cpu, mem or swap using command top.
[check_disk](https://github.com/rafaelurrutiasilva/nagios-bash-plugins/blob/main/plugins/check_disk) | Will check disk utilization.
[check_file_age](https://github.com/rafaelurrutiasilva/nagios-bash-plugins/blob/main/plugins/check_file_age) | Will check file age in min filter by name and numbers of files.
[check_ps](https://github.com/rafaelurrutiasilva/nagios-bash-plugins/blob/main/plugins/check_ps) | Will check linux process.


## Where to install
You can place the files anywhere in the file system, but two recommended locations are `/usr/local/nagios/libexec/` and `/opt/nagios/plugins/`. Alternatively, you are welcome to use the provided spec file to build an RPM package and then install it using the RPM package manager.

## Use RPM package
You can use the existing spec file to create an RPM package. The files will then be installed in the specified path: `/code>/usr/local/nagios/libexec/`.

