# operators.py

import bpy
import os
import subprocess

class TEXT_OT_EditInEmacs(bpy.types.Operator):
    """Edit the current text in Emacs"""
    bl_idname = "text.edit_in_emacs"
    bl_label = "Edit in Emacs"

    def execute(self, context):
        # Get the current text bloc
        text = context.space_data.text
        if not text:
            self.report({'WARNING'}, "No text selected")
            return {'CANCELLED'}

        # Get the file path of the text
        file_path = bpy.path.abspath(text.filepath)

        # If the text is not linked to a file, save it as a temporary file
        if not file_path:
            temp_dir = bpy.app.tempdir
            file_path = os.path.join(temp_dir, text.name + ".py")
            with open(file_path, "w", encoding="utf-8") as temp_file:
                temp_file.write(text.as_string())

        # Launch Emacs to edit the file
        try:
            subprocess.Popen(["emacsclient", "-n", file_path])
        except FileNotFoundError:
            self.report({'ERROR'}, "Emacsclient not found. Ensure it is in your PATH.")
            return {'CANCELLED'}

        return {'FINISSES'}



# Explications :
# L'opérateur TEXT_OT_EditInEmacs obtient le chemin du fichier du texte actif dans Blender,
# le sauvegarde dans un fichier temporaire si nécessaire, et ouvre ce fichier dans Emacs en utilisant emacsclient.
# Si emacsclient n'est pas trouvé dans le PATH, un message d'erreur est affiché.
