#   ef-create-background.py Copyright (C) 2020  Harshil Patel

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.




import random
import inkex
from lxml import etree

class CreateBackgrond(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument("--create", action='store', dest='create',
                                     type=bool, default=True, help='Create Background')

    def effect(self):
        
        if self.options.create:

            get_root = self.document.getroot()

            # self.createGuide(82.328, 152.538, 90.000)

            width  = self.svg.unittouu(get_root.get('width'))
            height = self.svg.unittouu(get_root.attrib['height'])

            layer = etree.SubElement(get_root, 'g')
            layer.set(inkex.addNS('label', 'inkscape'), 'Background-%d' %(random.randint(1,100)))
            layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

            style = {
                'stroke'        : 'none',
                'stroke-width'  : '1',
                'fill'          : '#000000'
            }
                    
            attribs = {
                'style'     : str(inkex.Style(style)),
                'height'    : str(height),
                'width'     : str(width),
                'x'         : str(0),
                'y'         : str(0)
            }

            parent = layer
            etree.SubElement(parent, inkex.addNS('rect','svg'), attribs )


if __name__ == '__main__':
    MyExtension = CreateBackgrond()
    MyExtension.run()