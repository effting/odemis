# -*- coding: utf-8 -*-
"""
Created on 1 Oct 2012

@author: Rinze de Laat

Copyright © 2012-2013 Rinze de Laat and Éric Piel, Delmic

This file is part of Odemis.

Odemis is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License version 2 as published by the Free
Software Foundation.

Odemis is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
Odemis. If not, see http://www.gnu.org/licenses/.

"""

from __future__ import division
from odemis.gui import model
from odemis.gui.model.stream import OPTICAL_STREAMS, EM_STREAMS, \
    SPECTRUM_STREAMS, AR_STREAMS
from odemis.gui.util import call_after
import collections
import logging
import wx

import odemis.gui.util.widgets as util

class ViewController(object):
    """ Manages the microscope view updates, change of viewport focus, etc.
    """

    def __init__(self, tab_data, main_frame, viewports):
        """
        tab_data (MicroscopyGUIData) -- the representation of the microscope GUI
        main_frame: (wx.Frame) -- the frame which contains the 4 viewports
        viewports (list of MicroscopeViewport or
                   OrderedDict (MicroscopeViewport -> kwargs)): the viewports to
          update. The first one is the one focused. If it's an OrderedDict, the
          kwargs are passed to the MicroscopeView creation. If there are more
          than 4 viewports, only the first 4 will be made visible and any others
          will be hidden.
        """
        self._data_model = tab_data
        self._main_data_model = tab_data.main

        if isinstance(viewports, collections.OrderedDict):
            self._viewports = viewports.keys()
            self._createViewsFixed(viewports)
        else:
            # create the (default) views
            self._viewports = viewports
            self._createViewsAuto()

        # First view is focused
        tab_data.focussedView.value = tab_data.visible_views.value[0]

        # Store the initial values, so we can reset
        self._def_views = tab_data.visible_views.value
        self._def_layout = tab_data.viewLayout.value
        self._def_focus = tab_data.focussedView.value

        # subscribe to layout and view changes
        tab_data.visible_views.subscribe(self._on_visible_views)
        tab_data.viewLayout.subscribe(self._onViewLayout, init=True)
        tab_data.focussedView.subscribe(self._onView, init=True)

    @property
    def viewports(self):
        return self._viewports

    def _createViewsFixed(self, viewports):
        """ Create the different views displayed, according to viewtypes
        viewports (OrderedDict (MicroscopeViewport -> kwargs)): cf init

        To be executed only once, at initialisation.

        FIXME: Since we have 2 different Views at the moments and probably more
        on the way, it's probably going to be beneficial to explicitly define
        them in the viewport data

        FIXME: Now views are created both in this method and in the
        _createViewsAuto method. It's probably best to have all stream creation
        done in the same place.
        """

        views = []
        visible_views = []

        for vp, vkwargs in viewports.items():
            # TODO: automatically set some clever values for missing arguments?
            # If stream classes are defined we assume a MicroscopeView is needed
            if 'stream_classes' in vkwargs:
                view = model.MicroscopeView(**vkwargs)
            else:
                view = model.View(**vkwargs)

            views.append(view)
            if vp.Shown:
                visible_views.append(view)

            vp.setView(view, self._data_model)

        self._data_model.views.value = views
        self._data_model.visible_views.value = visible_views

    def _createViewsAuto(self):
        """ Create the different views displayed, according to the current
        microscope.

        To be executed only once, at initialisation.
        """

        # If AnalysisTab for Sparc: SEM/Spec/AR/SEM
        assert not self._data_model.views.value # should still be empty
        if isinstance(self._data_model, model.AnalysisGUIData):
            assert len(self._viewports) >= 4
            # TODO: should be dependent on the type of acquisition, and so
            # updated every time the .file changes
            if self._main_data_model.role == "sparc":
                logging.info("Creating (static) SPARC viewport layout")
                vpv = collections.OrderedDict([
                    (self._viewports[0],  # focused view
                     {"name": "SEM",
                      "stream_classes": EM_STREAMS,
                      }),
                    (self._viewports[1],
                     {"name": "Spectrum",
                      "stream_classes": OPTICAL_STREAMS + SPECTRUM_STREAMS,
                      }),
                    (self._viewports[2],
                     {"name": "Angle resolved",
                      "stream_classes": AR_STREAMS,
                      }),
                    (self._viewports[3],
                     {"name": "SEM CL",
                      "stream_classes":
                            EM_STREAMS + OPTICAL_STREAMS + SPECTRUM_STREAMS,
                      }),
                ])
                self._createViewsFixed(vpv)
            else:
                logging.info("Creating generic static viewport layout")
                vpv = collections.OrderedDict([
                (self._viewports[0],  # focused view
                 {"name": "SEM",
                  "stream_classes": EM_STREAMS,
                  }),
                (self._viewports[1],
                 {"name": "Optical",
                  "stream_classes": OPTICAL_STREAMS + SPECTRUM_STREAMS,
                  }),
                (self._viewports[2],
                 {"name": "Combined 1",
                  "stream_classes":
                        EM_STREAMS + OPTICAL_STREAMS + SPECTRUM_STREAMS,
                  }),
                (self._viewports[3],
                 {"name": "Combined 2",
                  "stream_classes":
                        EM_STREAMS + OPTICAL_STREAMS + SPECTRUM_STREAMS,
                  }),
                (self._viewports[4],
                 {"name": "Spectrum",
                 }),
                                               ])
                self._createViewsFixed(vpv)

        # If SEM only: all SEM
        # Works also for the Sparc, as there is no other emitter, and we don't
        # need to display anything else anyway
        elif self._main_data_model.ebeam and not self._main_data_model.light:
            logging.info("Creating SEM only viewport layout")
            i = 1

            views = []
            visible_views = []

            for viewport in self._viewports:
                view = model.MicroscopeView(
                            "SEM %d" % i,
                            self._main_data_model.stage,
                            focus0=None, # TODO: SEM focus or focus1?
                            stream_classes=EM_STREAMS
                         )
                self._data_model.views.value.append(view)
                viewport.setView(view, self._data_model)
                i += 1

                views.append(view)
                if viewport.Shown:
                    visible_views.append(view)

            self._data_model.views.value = views
            self._data_model.visible_views.value = visible_views

        # If Optical only: all Optical
        # TODO: first one is brightfield only?
        elif not self._main_data_model.ebeam and self._main_data_model.light:
            logging.info("Creating Optical only viewport layout")
            i = 1

            views = []
            visible_views = []

            for viewport in self._viewports:
                view = model.MicroscopeView(
                            "Optical %d" % i,
                            self._main_data_model.stage,
                            focus0=self._main_data_model.focus,
                            stream_classes=OPTICAL_STREAMS
                         )
                self._data_model.views.value.append(view)
                viewport.setView(view, self._data_model)
                i += 1

                views.append(view)
                if viewport.Shown:
                    visible_views.append(view)

            self._data_model.views.value = views
            self._data_model.visible_views.value = visible_views

        # If both SEM and Optical (=SECOM): SEM/Optical/2x combined
        elif (self._main_data_model.ebeam and
              self._main_data_model.light and
              len(self._viewports) == 4):
            logging.info("Creating combined SEM/Optical viewport layout")
            vpv = collections.OrderedDict([
            (self._viewports[0],  # focused view
             {"name": "SEM",
              "stage": self._main_data_model.stage,
              "focus0": None, # TODO: SEM focus
              "stream_classes": EM_STREAMS,
              }),
            (self._viewports[1],
             {"name": "Optical",
              "stage": self._main_data_model.stage,
              "focus1": self._main_data_model.focus,
              "stream_classes": OPTICAL_STREAMS,
              }),
            (self._viewports[2],
             {"name": "Combined 1",
              "stage": self._main_data_model.stage,
              "focus0": None, # TODO: SEM focus
              "focus1": self._main_data_model.focus,
            "stream_classes": EM_STREAMS + OPTICAL_STREAMS,
              }),
            (self._viewports[3],
             {"name": "Combined 2",
              "stage": self._main_data_model.stage,
              "focus0": None, # TODO: SEM focus
              "focus1": self._main_data_model.focus,
            "stream_classes": EM_STREAMS + OPTICAL_STREAMS,
              }),
                                           ])
            self._createViewsFixed(vpv)
        else:
            logging.warning("No known microscope configuration, creating %d "
                            "generic views", len(self._viewports))
            i = 1
            for viewport in self._viewports:
                view = model.MicroscopeView(
                            "View %d" % i,
                            self._main_data_model.stage,
                            focus0=self._main_data_model.focus
                         )
                self._data_model.views.value.append(view)
                viewport.setView(view, self._data_model)
                i += 1

        # TODO: if chamber camera: br is just chamber, and it's the focussedView

    def _viewport_by_view(self, view):
        """ Return the ViewPort associated with the given view
        """

        for vp in self._viewports:
            if vp.microscope_view == view:
                return vp
        raise ValueError("No ViewPort found for view %s" % view)

    def _viewport_index_by_view(self, view):
        """ Return the index number of the ViewPort associated with the given
        view
        """
        return self._viewports.index(self._viewport_by_view(view))

    def reset(self, views=None):
        """ Reset the view layout

        This means that the viewport order, the viewport layout and the focus
        will all be reset to as they were when the controller was created.
        """

        containing_window = self._viewports[0].Parent
        containing_window.Freeze()

        try:
            # Reset the order of the viewports
            for i, def_view in enumerate(views or self._def_views):
                # If a viewport has moved compared to the original order...
                if self._viewports[i].microscope_view != def_view:
                    # ...put it back in its original place
                    j = self._viewport_index_by_view(def_view)
                    self.swap_viewports(i, j)

            # Reset the focus
            self._data_model.focussedView.value = self._def_focus
            # Reset the layout
            self._data_model.viewLayout.value = self._def_layout
        finally:
            containing_window.Thaw()

    def swap_viewports(self, vpi1, vpi2):
        """ Swap the positions of viewports denoted by indices vpi1 and vpi2

        It is assumed that vpi1 points to one of the viewports visible in a 2x2
        display, and that vpi2 is outside this 2x2 layout and invisible.
        """

        # Small shothand local variable
        vp = self._viewports

        # Get the sizer of the visible viewport
        sizer1 = vp[vpi1].GetContainingSizer()
        # And the one of the invisible one, which should be the containing sizer
        # of sizer1
        sizer2 = parent_sizer = vp[vpi2].GetContainingSizer()

        # Get the sizer position of the first viewport, so we can use that
        # to insert the other viewport
        pos1 = util.get_sizer_position(vp[vpi1])

        # Get the sizer item for the visible viewport, so we can access its
        # sizer properties like proportion and flags
        item1 = parent_sizer.GetItem(vp[vpi1], recursive=True)

        # Move viewport 2 to sizer 1
        sizer2.Detach(vp[vpi2])
        sizer1.Insert(
            pos1,
            vp[vpi2],
            proportion=item1.GetProportion(),
            flag=item1.GetFlag(),
            border=item1.GetBorder())

        # Move viewport 1 to the end of the conaining sizer
        sizer1.Detach(vp[vpi1])
        parent_sizer.Add(vp[vpi1])

        # Flip the visibility
        vp[vpi1].Hide()
        vp[vpi2].Show()

        # Swap the viewports in the viewport list
        vp[vpi1], vp[vpi2] = vp[vpi2], vp[vpi1]

        # Refresh the Layout
        parent_sizer.Layout()

    def _on_visible_views(self, visible_views):
        """ This method is called when the visible views in the data model
        change.
        """

        logging.debug("Visible view change detected")
        # Test if all provided views are known
        for view in visible_views:
            if view not in self._data_model.views.value:
                raise ValueError("Unknown view %s!" % view)

        self.reset(visible_views)

    def _onView(self, view):
        """ Called when another focussed view changes.

        :param view: (MicroscopeView) The newly focussed view
        """
        logging.debug("Changing focus to view %s", view.name.value)
        layout = self._data_model.viewLayout.value

        self._viewports[0].Parent.Freeze()

        try:
            for viewport in self._viewports:
                if viewport.microscope_view == view:
                    viewport.SetFocus(True)
                    if layout == model.VIEW_LAYOUT_ONE:
                        # TODO: maybe in that case, it's not necessary to display
                        # the focus frame around?
                        viewport.Show()
                else:
                    viewport.SetFocus(False)
                    if layout == model.VIEW_LAYOUT_ONE:
                        viewport.Hide()

            if layout == model.VIEW_LAYOUT_ONE:
                self._viewports[0].Parent.Layout() # resize viewport
        finally:
            self._viewports[0].Parent.Thaw()

    def _onViewLayout(self, layout):
        """ Called when the view layout of the GUI must be changed

        This method only manipulates ViewPort, since the only thing it needs to
        change is the visibility of ViewPorts.
        """

        containing_window = self._viewports[0].Parent

        containing_window.Freeze()

        try:
            if layout == model.VIEW_LAYOUT_ONE:
                logging.debug("Showing only one view")
                for viewport in self._viewports:
                    if viewport.microscope_view == self._data_model.focussedView.value:
                        viewport.Show()
                    else:
                        viewport.Hide()
            elif layout == model.VIEW_LAYOUT_22:
                logging.debug("Showing all views")
                # We limit the showing of viewports to the first 4, because more
                # than 4 may be present
                for viewport in self._viewports[:4]:
                    viewport.Show()

            elif layout == model.VIEW_LAYOUT_FULLSCREEN:
                raise NotImplementedError()
            else:
                raise NotImplementedError()

            containing_window.Layout()  # resize the viewports
        finally:
            containing_window.Thaw()

    def fitCurrentViewToContent(self):
        """
        Adapts the scale (MPP) of the current view to the content
        """
        # find the viewport corresponding to the current view
        for vp in self._viewports:
            if vp.microscope_view == self._data_model.focussedView.value:
                vp.canvas.fitViewToContent()
                break
        else:
            logging.error("Failed to find the current viewport")

class ViewSelector(object):
    """ This class controls the view selector buttons and labels associated with
    them.
    """

    def __init__(self, tab_data, main_frame, buttons):
        """
        tab_data (MicroscopyGUIData): the representation of the microscope
            GUI
        main_frame: (wx.Frame): the frame which contains the 4 viewports
        buttons (OrderedDict : btn -> (viewport, label)): 5 buttons and the
            viewport (for the image) and label (for changing the name)
            associated.
            The first button has no viewport, for the 2x2 view.
        """
        self._data_model = tab_data

        self.buttons = buttons

        for btn in self.buttons:
            btn.Bind(wx.EVT_BUTTON, self.OnClick)

        # subscribe to thumbnails
        self._subscriptions = [] # list of functions

        # subscribe to change of name
        for btn, (vp, lbl) in self.buttons.items():
            if vp is None: # 2x2 layout
                lbl.SetLabel("Overview")
                continue

            @call_after
            def onThumbnail(im, btn=btn): # save btn in scope
                btn.set_overlay(im)

            vp.microscope_view.thumbnail.subscribe(onThumbnail, init=True)
            # keep ref of the functions so that they are not dropped
            self._subscriptions.append(onThumbnail)

            # also subscribe for updating the 2x2 button
            vp.microscope_view.thumbnail.subscribe(self._update22Thumbnail)

            def onName(name, lbl=lbl): # save lbl in scope
                lbl.SetLabel(name)

            vp.microscope_view.name.subscribe(onName, init=True)
            self._subscriptions.append(onName)

        # subscribe to layout and view changes
        self._data_model.viewLayout.subscribe(self._onViewChange)
        self._data_model.focussedView.subscribe(self._onViewChange, init=True)

    def toggleButtonForView(self, microscope_view):
        """
        Toggle the button which represents the view and untoggle the other ones
        microscope_view (MicroscopeView or None): the view, or None if the first
                                    button (2x2) is to be toggled
        Note: it does _not_ change the view
        """
        for b, (vp, lbl) in self.buttons.items():
            # 2x2 => vp is None / 1 => vp exists and vp.view is the view
            if ((vp is None and microscope_view is None) or
                (vp and vp.microscope_view == microscope_view)):
                b.SetToggle(True)
            else:
                if vp:
                    logging.debug("untoggling button of view %s",
                                  vp.microscope_view.name.value)
                else:
                    logging.debug("untoggling button of view All")
                b.SetToggle(False)

    @call_after
    def _update22Thumbnail(self, im):
        """
        Called when any thumbnail is changed, to recompute the 2x2 thumbnail of
        the first button.
        im (unused)
        """

        # Create an image from the 4 thumbnails in a 2x2 layout with small
        # border. The button without a viewport attached is assumed to be the
        # one assigned to the 2x2 view
        btn_all = [b for b, (vp, lbl) in self.buttons.items() if vp is None][0]
        border_width = 2 # px
        size = max(1, btn_all.overlay_width), max(1, btn_all.overlay_height)
        size_sub = (max(1, (size[0] - border_width) // 2),
                    max(1, (size[1] - border_width) // 2))
        # starts with an empty image with the border colour everywhere
        im_22 = wx.EmptyImage(*size, clear=False)
        im_22.SetRGBRect(wx.Rect(0, 0, *size),
                         *btn_all.GetBackgroundColour().Get())

        i = 0

        for vp, lbl in self.buttons.values():
            if vp is None: # 2x2 layout
                continue

            im = vp.microscope_view.thumbnail.value
            if im:
                # im doesn't have the same aspect ratio as the actual thumbnail
                # => rescale and crop on the center
                # Rescale to have the smallest axis as big as the thumbnail
                rsize = list(size_sub)
                if (size_sub[0] / im.Width) > (size_sub[1] / im.Height):
                    rsize[1] = int(im.Height * (size_sub[0] / im.Width))
                else:
                    rsize[0] = int(im.Width * (size_sub[1] / im.Height))
                sim = im.Scale(*rsize, quality=wx.IMAGE_QUALITY_HIGH)

                # crop to the right shape
                lt = ((size_sub[0] - sim.Width) // 2,
                      (size_sub[1] - sim.Height) // 2)
                sim.Resize(size_sub, lt)

                # compute placement
                y, x = divmod(i, 2)
                # copy im in the right place
                im_22.Paste(sim,
                            x * (size_sub[0] + border_width),
                            y * (size_sub[1] + border_width))
            else:
                # black image
                # Should never happen
                pass #sim = wx.EmptyImage(*size_sub)

            i += 1

        # set_overlay will rescale to the correct button size
        btn_all.set_overlay(im_22)

    def _onViewChange(self, unused):
        """
        Called when another view is focused, or viewlayout is changed
        """
        logging.debug("Updating view selector")

        # TODO when changing from 2x2 to a view non focused, it will be called
        # twice in row. => optimise to not do it twice

        if self._data_model.viewLayout.value == model.VIEW_LAYOUT_22:
            # (layout is 2x2) => select the first button
            self.toggleButtonForView(None)
        else:
            # otherwise (layout is 1) => select the right button
            self.toggleButtonForView(self._data_model.focussedView.value)


    def OnClick(self, evt):
        """
        Navigation button click event handler

        Show the related view(s) and sets the focus if needed.
        """

        # The event does not need to be 'skipped' because
        # the button will be toggled when the event for value change is
        # received.

        btn = evt.GetEventObject()
        viewport = self.buttons[btn][0]

        if viewport is None:
            # 2x2 button
            # When selecting the overview, the focussed viewport should not
            # change
            self._data_model.viewLayout.value = model.VIEW_LAYOUT_22
        else:
            # It's preferable to change the view before the layout so that
            # if the layout was 2x2 with another view focused, it doesn't first
            # display one big view, and immediately after changes to another
            # view.
            self._data_model.focussedView.value = viewport.microscope_view
            self._data_model.viewLayout.value = model.VIEW_LAYOUT_ONE
