import os
import rclpy
from ament_index_python.packages import get_package_share_directory

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget

from mission_mode.srv import MissionModeChange

# Must match values in MissionModeChange
START = 1
END   = 2
KILL  = 3

class MissionModePlugin(Plugin):

    def __init__(self, context):
        super(MissionModePlugin, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MissionModePlugin')  

        # Create QWidget
        self._widget = QWidget()

        # Get path to UI file which should be in the "resource" folder of this package
        ui_file = os.path.join(get_package_share_directory('behavior_selector2'), 'resource', 'MissionModePlugin.ui')
        # Extend the widget with all attributes and children from UI file
        loadUi(ui_file, self._widget)
        # Give QObjects reasonable names
        self._widget.setObjectName('MissionModePluginUi')
        # Show _widget.windowTitle on left-top of each plugin (when 
        # it's set in _widget). This is useful when you open multiple 
        # plugins at once. Also if you open multiple instances of your 
        # plugin at once, these lines add number to make it easy to 
        # tell from pane to pane.
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        # Add widget to the user interface
        context.add_widget(self._widget)

        self._widget.start_push_button.pressed.connect(self._on_start_pressed)
        self._widget.end_push_button.pressed.connect(self._on_end_pressed)
        self._widget.stop_push_button.pressed.connect(self._on_stop_pressed)

        # To start client
        self.node = None
        self.client = None

    def _on_start_pressed(self):
        mode = START
        self._change_mode(mode)

    def _on_end_pressed(self):
        mode = END
        self._change_mode(mode)

    def _on_stop_pressed(self):
        mode = KILL
        self._change_mode(mode)

    def _change_mode(self,mode):
        if self.client == None: 
            rclpy.init()
            self.node = rclpy.create_node('mode_client')
            self.client = self.node.create_client(MissionChangeMode, "change_mode")
        
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.node.get_logger().info('MissionChangeMode service not available, waiting again...')
        resp = self.client.call_async(mode) 
        rclpy.spin_until_future_complete(self.node, mode)
    
