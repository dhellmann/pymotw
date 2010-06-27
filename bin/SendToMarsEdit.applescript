
on read_file(filename)
	set filehandle to (open for access (POSIX file filename))
	set post_body to (read filehandle for (get eof filehandle))
	return post_body
end read_file

on load_post(title_text, body_text)
	tell application "MarsEdit"
		activate
		set post_window to make new document
		tell post_window
			set the body to body_text
			set category names to {"PyMOTW", "python"}
		end tell
		
		(* Changing these values seems to modify the identity of the window, so change them and refer to the document by id. *)
		set current weblog of document 1 to weblog "Doug Hellmann"
		set the title of document 1 to title_text
	end tell
end load_post

on run argv
	set filename to item 1 of argv
	set title_text to item 2 of argv
	set body_text to read_file(filename)
	load_post(title_text, body_text)
end run
