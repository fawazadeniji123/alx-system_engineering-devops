file 0-iam_betty is a script that switches the current user to the user betty

file 1-who_am_i is a script that prints the effective username of the current user.

file 2-groups is a script that prints all the groups the current user is part of.

file 3-new_owner is a script that changes the owner of the file hello to the user betty.

file 4-empty is a script that creates an empty file called hello.

file 5-execute is a script that adds execute permission to the owner of the file hello.

file 6-multiple_permissions is a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

file 7-everybody is a script that adds execution permission to the owner, the group owner and the other users, to the file hello.

file 8-James_Bond is a script that sets the permission to the file hello as follows:



  * Owner: no permission at all

  * Group: no permission at all

  * Other users: all the permissions

file 9-John_Doe is a script that sets the  mode of the file hello to this:



  `-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`

file 10-mirror_permissions is a script that sets the mode of the file hello to hello the same as olleh's mode.

file 11-directories_permissions is a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed

file 12-directory_permissions is a script that creates a directory called my_dir with permissions 751 in the working directory.

file 13-change_group is a script that changes the group owner to school for the file hello.

file 100-change_owner_and_group is a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

file 101-symbolic_link_permissions is a script that changes the owner and the group owner of _hello to vincent and staff respectively.



  * The file _hello is a symbolic link

file 102-if_only is a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
