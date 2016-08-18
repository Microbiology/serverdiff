import filecmp
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-f', '--first')
parser.add_argument('-s', '--second')

args = parser.parse_args()

from filecmp import dircmp
def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print "Shared file with different content %s found in %s and %s" % (name, dcmp.left, dcmp.right)
    for name in dcmp.diff_files:
        if dcmp.left_only : print "Directory %s uniquely contains %s" % (dcmp.left, dcmp.left_only)
        if dcmp.right_only : print "Directory %s uniquely contains %s" % (dcmp.right, dcmp.right_only)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

dcmp = dircmp(args.first, args.second)

print_diff_files(dcmp) 
