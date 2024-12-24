# operators.py

import bpy
import os
import subprocess

class EditInEmacsOperator(bpy.types.Operator):
    bl_idname = "text.edit_in_emacs"
    bl_label = "Edit in Emacs"
    bl_description = "Edit the selected text in Emacs"

    @classmethod
    def poll(cls, context):
        # L'opérateur est actif uniquement s'il y a des textes disponibles
        return len(bpy.data.texts) > 0

    def execute(self, context):
        # Get the current text bloc
        text = context.space_data.text
        if text is None:
            self.report({'WARNING'}, "No text selected")
            return {'CANCELLED'}

        # Get the file path of the text
        file_path = bpy.path.abspath(text.filepath)
        if not file_path:
            self.report({'WARNING'}, "Text has no file path")
            return {'CANCELLED'}

        # Commande pour ouvrir le fichier dans Emacs
        try:
            subprocess.Popen(["emacsclient", "-n", file_path])
            self.report({'INFO'}, f"Editing {text.name} in Emacs")
            return {'FINISHED'}
        except FileNotFoundError:
            self.report({'ERROR'}, "Emacsclient not found. Ensure it is in your PATH.")
            return {'CANCELLED'}
