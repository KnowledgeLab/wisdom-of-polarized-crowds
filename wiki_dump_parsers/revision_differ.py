#!/usr/local/bin/pypy
################################################################################
# Revision Differ
#
# This script was written to be a streaming mapper for wikihadoop
# (see https://github.com/whym/wikihadoop).  By default, this script runs under
# pypy (much faster), but it can also be run under CPython 2.7+.
#
# Required to run this script are
#  - diff_match_patch.py (provided)
#  - xml_simulator.py (provided)
#  - wikimedia-utilities (https://bitbucket.org/halfak/wikimedia-utilities)
#
# Author: Aaron Halfaker (aaron.halfaker@gmail.com)
#
# This software licensed as GPLv2(http://www.gnu.org/licenses/gpl-2.0.html). and
# is provided WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
#
################################################################################
import re
from io import StringIO
from diff_match_patch import diff_match_patch

def tokenize(content):
	return re.findall(
		r"[\w]+" +   #Word
		r"|\[\[" +   #Opening internal link
		r"|\]\]" +   #Closing internal link
		r"|\{\{" +   #Opening template
		r"|\}\}" +   #Closing template
		r"|\{\{\{" + #Opening template var
		r"|\}\}\}" + #Closing template var
		r"|\n+" +    #Line breaks
		r"| +" +     #Spaces
		r"|&\w+;" +  #HTML escape sequence
		r"|'''" +    #Bold
		r"|''" +     #Italics
		r"|=+" +     #Header
		r"|\{\|" +   #Opening table
		r"|\|\}" +   #Closing table
		r"|\|\-" +   #Table row
		r"|.",       #Misc character
		content
	)

def hashTokens(tokens, hash2Token=[], token2Hash={}):
	hashBuffer = StringIO()
	for t in tokens:
		if t in token2Hash:
			hashBuffer.write(chr(token2Hash[t]+1))
		else:
			hashId = len(hash2Token)
			hash2Token.append(t)
			token2Hash[t] = hashId
			hashBuffer.write(chr(hashId+1))

	return (hashBuffer.getvalue(), hash2Token, token2Hash)

def unhash(hashes, hash2Token, sep=''):
	return sep.join(hash2Token[ord(h)-1] for h in hashes)

def simpleDiff(content1, content2, tokenize=tokenize, sep=''):
	hashes1, h2t, t2h = hashTokens(tokenize(content1))
	hashes2, h2t, t2h = hashTokens(tokenize(content2), h2t, t2h)

	dmp = diff_match_patch()
	diffs = dmp.diff_main(hashes1, hashes2, checklines=False)

	added=' '.join([unhash(hashes,h2t,sep=sep) for (ar,hashes) in diffs if ar==1])
	return added
