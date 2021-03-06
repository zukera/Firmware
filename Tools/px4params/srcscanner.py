import os
import re
import codecs

class SourceScanner(object):
    """
    Traverses directory tree, reads all source files, and passes their contents
    to the Parser.
    """

    def ScanDir(self, srcdir, parser):
        """
        Scans provided path and passes all found contents to the parser using
        parser.Parse method.
        """
        extensions = tuple(parser.GetSupportedExtensions())
        for dirname, dirnames, filenames in os.walk(srcdir):
            for filename in filenames:
                if filename.endswith(extensions):
                        path = os.path.join(dirname, filename)
                        self.ScanFile(path, parser)

    def ScanFile(self, path, parser):
        """
        Scans provided file and passes its contents to the parser using
        parser.Parse method.
        """
        with codecs.open(path, 'r', 'utf-8') as f:
            contents = f.read()
        parser.Parse(contents)
