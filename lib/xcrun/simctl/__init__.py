"""Wrapper around `xcrun simctl`."""

from xcrun.simctl.simctl import *
import xcrun.simctl.device_pair
import xcrun.simctl.device_type
import xcrun.simctl.device
import xcrun.simctl.listall
import xcrun.simctl.runtime


#	create              Create a new device.
#	clone               Clone an existing device.
#	upgrade             Upgrade a device to a newer runtime.
#	delete              Delete a device or all unavailable devices.
#	pair                Create a new watch and phone pair.
#	unpair              Unpair a watch and phone pair.
#	pair_activate       Set a given pair as active.
#	erase               Erase a device's contents and settings.
#	boot                Boot a device.
#	shutdown            Shutdown a device.
#	rename              Rename a device.
#	install             Install an app on a device.
#	uninstall           Uninstall an app from a device.
#	terminate           Terminate an application by identifier on a device.

# Advanced:

#	pbsync              Sync the pasteboard content from one pasteboard to another.
#	pbcopy              Copy standard input onto the device pasteboard.
#	pbpaste             Print the contents of the device's pasteboard to standard output.
#	io                  Set up a device IO operation.
#	spawn               Spawn a process on a device.
#	launch              Launch an application by identifier on a device.


# DONE:

#	addmedia            Add photos, live photos, or videos to the photo library of a device
#	get_app_container   Print the path of the installed app's container
#	getenv              Print an environment variable from a running device.
#	icloud_sync         Trigger iCloud sync on a device.
#	list                List available devices, device types, runtimes, or device pairs.
#	logverbose          enable or disable verbose logging for a device
#	openurl             Open a URL in a device.


# Won't Do:

#	diagnose            Collect diagnostic information and logs.
#	help                Prints the usage for a given subcommand.
