#!/usr/bin/env python

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


"""
This extension creates the exact canvas size rectangle as a background layer.
Version dev-2.2
"""
import random
import inkex


class CreateBackground(inkex.GenerateExtension):

    @staticmethod
    def add_arguments(pars):
        """
        Taking an arguments from user from GUI options.
        """
        pars.add_argument("--create_background",
                          type=inkex.Boolean, default=True, help='Create Background')
        pars.add_argument("--background_color",
                          type=inkex.Color, default='#000000FF', help='Select Background Color')
        pars.add_argument("--lock_layer",
                          type=inkex.Boolean, help='Lock Layer')

    container_layer = True
    container_label = 'Background-%d' % (random.randint(1, 100))

    def generate(self):
        """
        Generating canvas size rectangle as a Background-%d.
        """
        style = {
            'stroke': 'none',
            'stroke-width': '1',
            'fill': self.options.background_color
        }

        child = inkex.Rectangle.new(0, 0, self.svg.width, self.svg.height)  # inkex.Rectangle.new(x, y, w, h)
        child.style = style
        yield child
        if self.options.lock_layer is True:
            child.getparent().set('sodipodi:insensitive', 'true')


if __name__ == '__main__':
    MyExtension = CreateBackground()
    MyExtension.run()
