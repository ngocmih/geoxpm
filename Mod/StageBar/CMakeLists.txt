# CMakeLists.txt - StageBar

# Xác định thư mục cài đặt cho StageBar
set(StageBar_INSTALL_DIR ${CMAKE_INSTALL_DATADIR}/FreeCAD/Mod/StageBar)

# Đảm bảo StageBar có trong thư mục build
file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/StageBar)

# Copy các file Python vào thư mục build trước khi cài đặt
file(COPY InitGui.py stagebar.py DESTINATION ${CMAKE_BINARY_DIR}/Mod/StageBar)

# Cài đặt vào thư mục FreeCAD Mod khi chạy `make install`
install(FILES 
    InitGui.py
    stagebar.py
    DESTINATION ${StageBar_INSTALL_DIR}
)
