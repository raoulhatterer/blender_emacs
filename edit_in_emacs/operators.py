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
        """Cette méthode est appelée par Blender avant d'afficher ou d'activer un opérateur dans l'interface utilisateur. Ici, l'opérateur est actif uniquement si len(bpy.data.texts) > 0, c'est-à-dire qu'il existe au moins un texte dans Blender."""
        return len(bpy.data.texts) > 0

    def execute(self, context):
        # Get the current text bloc
        text = context.space_data.text
        if text is None:
            self.report({'WARNING'}, "No text selected")
            return {'CANCELLED'}

        temp_dir = bpy.app.tempdir
        file_path = os.path.join(temp_dir, f"blender_{text.name}.py")
        with open(file_path, "w", encoding="utf-8") as temp_file:
            temp_file.write(text.as_string())


    

        # Commande pour ouvrir le fichier dans Emacs
        try:
            subprocess.Popen(["emacsclient", "-n", file_path])
            self.report({'INFO'}, f"Editing {text.name} in Emacs")
            return {'FINISHED'}
        except FileNotFoundError:
            self.report({'ERROR'}, "Emacsclient not found. Ensure it is in your PATH.")
            return {'CANCELLED'}
