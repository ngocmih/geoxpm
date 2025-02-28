// NATAES Ngoc 2.2025
#include "StageView.h"
#include <QVBoxLayout>
#include <QLabel>

#include <QTreeWidget>

#include <Base/Console.h>
#include <Base/Parameter.h>  // 🔹 Fix lỗi: Thiếu khai báo quản lý tham số
#include <sstream>           // 🔹 Fix lỗi: Thiếu khai báo xử lý chuỗi
#include <App/Application.h>

using namespace Gui;
using namespace Gui::DockWnd;

StageView::StageView(QWidget* parent)
    : QDockWidget(parent)
{
    auto widget = new QWidget(this);
    auto layout = new QVBoxLayout(widget);

    // Tieu de hien thi
    auto label = new QLabel(tr("Stage View"), widget);
    layout->addWidget(label);

    // hien thi danh sach tung stage
    treeWidget = new QTreeWidget(widget);
    treeWidget->setColumnCount(1);
    treeWidget->setHeaderLabel(tr("Objects in Stage"));
    layout->addWidget(treeWidget);

    widget->setLayout(layout);
    setWidget(widget);

    connect(treeWidget, &QTreeWidget::itemClicked, this, &StageView::toggleItemExpansion);
}

StageView::~StageView() = default;

void StageView::updateStageActionsFromList(const QStringList& actionList)
{
    treeWidget->clear();

    // Giả sử stage hiện tại là "StagedConstruction" (có thể thay đổi tùy yêu cầu)
    QString rootText = tr("StagedConstruction");
    QTreeWidgetItem* rootItem = new QTreeWidgetItem(treeWidget);
    rootItem->setText(0, rootText);
    treeWidget->addTopLevelItem(rootItem);

    // Thêm các object (actions) dưới dạng node con của rootItem
    for (const QString& action : actionList) {
        QTreeWidgetItem* child = new QTreeWidgetItem();
        child->setText(0, action);
        rootItem->addChild(child);
    }

    // Thu gọn cây (chỉ hiển thị node gốc), để khi click sẽ mở rộng
    treeWidget->collapseItem(rootItem);
}
void StageView::toggleItemExpansion(QTreeWidgetItem* item, int column)
{
    // Chỉ toggle nếu mục có con
    if (item->childCount() > 0) {
        if (treeWidget->isItemExpanded(item)) {
            treeWidget->collapseItem(item);
        }
        else {
            treeWidget->expandItem(item);
        }
    }
}
// NATAES Ngoc 2.2025