#!/usr/bin/perl

use strict;
use warnings;
use Data::Dumper;


#my $res = `../../../../pyx/pathdefgen.pl NE 1`;


open my $fh, '<', 'svsd_list.csv' or die $!;

my $line = <$fh>;
chomp $line;
my @field_names = split /,/, $line;

while ($line = <$fh>) {
    chomp $line;
    my %fields;
    @fields{@field_names} = split /,/, $line;
    #print Dumper \%fields;
    if (-f "$fields{'符号名アルファベット表記'}.py") {
        print "$fields{'符号名アルファベット表記'}.py exists\n"; 
    }
    else {
        my $filename = "$fields{'符号名アルファベット表記'}.py";
        print "$filename does not exist\n"; 
        my $model_wo_numbers;
        ($model_wo_numbers = $fields{'モデル表記'}) =~ s/\d//g;
        $model_wo_numbers = "$fields{'モデル表記'}" if $model_wo_numbers eq '';
        #print $model_wo_numbers, "\n";

        open my $fh, '>', $filename or die $!;
        print $fh template(@fields{'クラス名', '符号名', '符号名アルファベット表記', 'モデル表記', '字頭区分', '字尾区分'});

        my $pathdef = `../../../../pyx/pathdefgen.pl $model_wo_numbers 1`;
        print $fh $pathdef;

        close $fh;
    }
}


close $fh;



sub template {
# '字尾区分' => 'S',
# '符号名アルファベット表記' => 'le',
# '符号名' => 'ぇ',
# '字頭区分' => 'NER',
# 'モデル表記' => 'UNR1S',
# 'クラス名' => 'CharLe'
#

my ($class, $name, $kana, $model, $head, $tail) = @_;

my $py = << "EOS";
from ..svsd.char import SvsdChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    knot,
    endknot,
    smoothknot,
    tensioncurve,
    controlcurve,
    curve)

class ${class}(SvsdChar):
    def __init__(self, name='$name', kana='$kana',
                 model='$model', head_type='$head', tail_type='$tail', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
EOS
}
