// NATAES Ngoc 2.2025
// #include "StageView.h"
// #include <QVBoxLayout>
// #include <QLabel>

// #include <QTreeWidget>

// #include <Base/Console.h>
// #include <Base/Parameter.h>  // 🔹 Fix lỗi: Thiếu khai báo quản lý tham số
// #include <sstream>           // 🔹 Fix lỗi: Thiếu khai báo xử lý chuỗi
// #include <App/Application.h>

// using namespace Gui;
// using namespace Gui::DockWnd;

// StageView::StageView(QWidget* parent)
//     : QDockWidget(parent)
// {
//     auto widget = new QWidget(this);
//     auto layout = new QVBoxLayout(widget);

//     // Tieu de hien thi
//     auto label = new QLabel(tr("Stage View"), widget);
//     layout->addWidget(label);

//     // hien thi danh sach tung stage
//     treeWidget = new QTreeWidget(widget);
//     treeWidget->setColumnCount(1);
//     treeWidget->setHeaderLabel(tr("Objects in Stage"));
//     layout->addWidget(treeWidget);

//     widget->setLayout(layout);
//     setWidget(widget);

//     connect(treeWidget, &QTreeWidget::itemClicked, this, &StageView::toggleItemExpansion);
// }

// StageView::~StageView() = default;

// void StageView::updateStageActionsFromList(const QStringList& actionList)
// {
//     treeWidget->clear();

//     // Giả sử stage hiện tại là "StagedConstruction" (có thể thay đổi tùy yêu cầu)
//     QString rootText = tr("StagedConstruction");
//     QTreeWidgetItem* rootItem = new QTreeWidgetItem(treeWidget);
//     rootItem->setText(0, rootText);
//     treeWidget->addTopLevelItem(rootItem);

//     // Thêm các object (actions) dưới dạng node con của rootItem
//     for (const QString& action : actionList) {
//         QTreeWidgetItem* child = new QTreeWidgetItem();
//         child->setText(0, action);
//         rootItem->addChild(child);
//     }

//     // Thu gọn cây (chỉ hiển thị node gốc), để khi click sẽ mở rộng
//     treeWidget->collapseItem(rootItem);
// }
// void StageView::toggleItemExpansion(QTreeWidgetItem* item, int column)
// {
//     // Chỉ toggle nếu mục có con
//     if (item->childCount() > 0) {
//         if (treeWidget->isItemExpanded(item)) {
//             treeWidget->collapseItem(item);
//         }
//         else {
//             treeWidget->expandItem(item);
//         }
//     }
// }
#include "StageView.h"
#include <QVBoxLayout>
#include <QListWidget>
#include <Gui/Application.h>
#include <Base/Console.h>
#include <boost/bind.hpp>

using namespace Gui;
using namespace Gui::DockWnd;

StageView::StageView(QWidget* parent)
    : QDockWidget(parent)
{
    // Thiết lập widget chính
    auto widget = new QWidget(this);
    auto layout = new QVBoxLayout(widget);

    listWidget = new QListWidget(widget);
    layout->addWidget(listWidget);
    widget->setLayout(layout);
    setWidget(widget);

    // Kết nối sự kiện nhấp chuột vào danh sách (Qt signal/slot)
    connect(listWidget, &QListWidget::itemClicked, this, &StageView::onItemClicked);

    // Kết nối signalSelectionChanged bằng boost::bind (FreeCAD signal)
    Gui::Selection().signalSelectionChanged.connect(
        boost::bind(&StageView::onSelectionChanged, this, _1));

    // Cập nhật danh sách ban đầu
    updateList();
}

StageView::~StageView()
{
    // Không cần gỡ kết nối vì boost::signals2 tự động quản lý lifetime
}

void StageView::onSelectionChanged(const Gui::SelectionChanges& msg)
{
    updateList();  // Cập nhật danh sách khi lựa chọn thay đổi
}

void StageView::updateList()
{
    listWidget->clear();  // Xóa danh sách cũ

    // Lấy danh sách các đối tượng được chọn
    std::vector<Gui::SelectionSingleton::SelObj> selections = Gui::Selection().getSelection();
    for (const auto& sel : selections) {
        const App::DocumentObject* obj = sel.pObject;  // Lấy con trỏ từ SelObj
        if (obj) {
            QListWidgetItem* item = new QListWidgetItem(QString::fromUtf8(obj->Label.getValue()));
            item->setData(
                Qt::UserRole,
                QVariant::fromValue(const_cast<App::DocumentObject*>(obj)));  // Loại bỏ const
            listWidget->addItem(item);
        }
    }
}

void StageView::onItemClicked(QListWidgetItem* item)
{
    // Lấy đối tượng từ item
    App::DocumentObject* obj = item->data(Qt::UserRole).value<App::DocumentObject*>();

    if (obj) {
        // Xóa lựa chọn hiện tại và chọn lại đối tượng
        Gui::Selection().clearSelection();
        Gui::Selection().addSelection(obj->getDocument()->getName(), obj->getNameInDocument());
    }
}
// NATAES Ngoc 2.2025