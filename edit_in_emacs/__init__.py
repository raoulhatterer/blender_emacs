# __init__.py
bl_info = {
    "name": "Edit in Emacs",
    "description": "Edit Blender scripts in Emacs",
    "author": "Raoul HATTERER",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "category": "Development",
}

# bl_info : dictionnaire qui contient les métadonnées de l'addon.

import bpy
from .operators import EditInEmacsOperator

# Dans operators.py on  définit l'opérateur qui ouvrira le fichier dans Emacs.

def register():
    """Enregistre l'opérateur et ajoute l'option au menu contextuel."""
    bpy.utils.register_class(EditInEmacsOperator)
    bpy.types.TEXT_MT_context_menu.append(menu_func)

def unregister():
    """Désenregistre l'opérateur et retire l'option du menu contextuel."""
    bpy.utils.unregister_class(EditInEmacsOperator)
    bpy.types.TEXT_MT_context_menu.remove(menu_func)

def menu_func(self, context):
    """Ajoute l'option "Edit in Emacs" au menu contextuel dans l'éditeur de texte de Blender."""
    self.layout.operator(EditInEmacsOperator.bl_idname)

if __name__ == "__main__":
    register()
    





