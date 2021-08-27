<h1> Nagios Plugins in Bash </h1>
<h2> Introduction </h2>
All plugins here are writen i bash script. They are tested in CentOS, Suse, RHEL and Photon OS.

<h2> How to use</h2>
Use the argument <code> --help </code> to get infrmation about how to use the plugins here.

<h2> Where to install</h2>
You can put the files whereever you want in the file system but one recommendation is the <code> /usr/local/nagios/libexec/ </code>. Other place can be <code> /opt/nagios/plugins/ </code>. You are also welome to use the spec-file and build the rpm-package and then install using that.

<h2> Use RPM package </h2>
You can use the existing spec-file to create an rpm-packege. The files will then be installed in path <code> /usr/local/nagios/libexec/ </code>.

