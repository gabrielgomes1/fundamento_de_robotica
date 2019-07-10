from PIL import Image

imagem = Image.open('carro.jpg')

size = width, heiht = imagem.size

saveFile = open('carro.txt', 'w')

inicio = """MODULE Module1
	CONST robtarget p0:=[[806.29,0.00,1154.00],[0.5,0,0.866025,0],[0,0,0,0],[9E+9,9E+9,9E+9,9E+9,9E+9,9E+9]];
	CONST robtarget p20:=[[806.29,0.00,1154.00],[0.5,0,0.866025,0],[0,0,0,0],[9E+9,9E+9,9E+9,9E+9,9E+9,9E+9]];
	CONST robtarget p10:=[[806.29,0.00,1154.00],[0.5,0,0.866025,0],[0,0,0,0],[9E+9,9E+9,9E+9,9E+9,9E+9,9E+9]];
    !***********************************************************
    !
    ! Module:  Module1
    !
    ! Description:
    !   <Insert description here>
    !
    ! Author: ufabc
    !
    ! Version: 1.0
    !
    !***********************************************************
    
    
    !***********************************************************
    !
    ! Procedure main
    !
    !   This is the entry point of your program
    !
    !***********************************************************
    PROC main()
        !Add your code here
        MoveJ p0, v100, z50, tool0;
        
"""

saveFile.write(inicio)

for x in range(width):
    for y in range(heiht):
        coordenadas = x, y
        if imagem.getpixel( coordenadas ) == (0, 0, 0):
            a = (x/30)
            b = (y/30)
            
            parteA = (f'\n\tMoveL Offs(p0,{a},{b},20), v10, z10, tool0;\n')
            parteB = (f'\tMoveL Offs(p0,{a},{b},0), v10, z10, tool0;\n')
            parteC = (f'\tMoveL Offs(p0,{a},{b},20), v10, z10, tool0;\n')

            saveFile.write(parteA)
            saveFile.write(parteB)
            saveFile.write(parteC)

final = """    ENDPROC
ENDMODULE"""

saveFile.write(final)
saveFile.close()
