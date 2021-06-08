#!/usr/bin/perl

use strict;
use DBI;

my $source = "DBI:mysql:demodb";
my $username = "root";
my $password = "";
my $dbc = DBI->connect($source, $username, $password);
my $sql = $dbc->prepare("select name, type from test");
my $out = $sql->execute();
while ((my $name,my $type) = $sql->fetchrow_array())
{
    print "Name: $name Type: $type\n";
} 