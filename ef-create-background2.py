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

class CreateBackgrond(inkex.GenerateExtension):

    def add_arguments(self, pars):
        pars.add_argument("--create", action='store', dest='create',
                                     type=inkex.Boolean, default=True, help='Create Background')
        pars.add_argument("--background_color",
                                     type=inkex.Color, default='#000000FF', help='Select Background Color')

    def generate(self):
        
        # if self.options.create:

        get_root = self.document.getroot()

        width  = self.svg.unittouu(get_root.get('width'))
        height = self.svg.unittouu(get_root.attrib['height'])

        layer = self.svg.add(inkex.Layer.new('Background-%d' %(random.randint(1,100))))

        style = {
            'stroke'        : 'none',
            'stroke-width'  : '1',
            'fill'          : self.options.background_color
        }

        parent = layer
        child = parent.add(inkex.Rectangle.new(0, 0, width, height)) # inkex.Rectangle.new(x, y, w, h)
        child.style = style

        return child


if __name__ == '__main__':
    MyExtension = CreateBackgrond()
    MyExtension.run()