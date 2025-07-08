import win32com.client
import os

def insert_image(excel_path, image_path, cell):
    vba_code = """
Sub InsertImage(cell As String)
    Dim lastShape As Shape
    Set lastShape = ActiveSheet.Shapes(ActiveSheet.Shapes.Count)
    lastShape.Select
    Selection.Copy
    Range(cell).Select
    Selection.PastePictureInCell
    lastShape.Delete
    ActiveWorkbook.Save
    
End Sub
"""

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False

    try:
        wb = excel.Workbooks.Open(os.path.abspath(excel_path))
        ws = wb.ActiveSheet
        target_cell = ws.Range("XFD1048576")

        shape = ws.Shapes.AddPicture(
            Filename=os.path.abspath(image_path),
            LinkToFile=False,
            SaveWithDocument=True,
            Left=target_cell.Left,
            Top=target_cell.Top,
            Width=target_cell.Width,
            Height=target_cell.Height
        )

        shape.Placement = 1
        # Accès à l'éditeur VBA
        vb_module = wb.VBProject.VBComponents.Add(1)  # 1 = standard module
        vb_module.CodeModule.AddFromString(vba_code)

        # Exécution de la macro
        excel.Application.Run("InsertImage", cell)

        wb.Save()
        wb.Close()
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        excel.Quit()



insert_image("assets\\test.xlsx", "assets\\star.jpg", "C5")