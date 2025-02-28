// NATAES Ngoc 2.2025
#ifndef GUI_STAGEVIEW_H
#define GUI_STAGEVIEW_H

#include <QDockWidget>
#include <QTreeWidget>

namespace Gui
{
namespace DockWnd
{

class StageView: public QDockWidget
{
    Q_OBJECT

public:
    explicit StageView(QWidget* parent = nullptr);
    ~StageView() override;
    // void updateStageActions();

public Q_SLOTS:
    // Slot để toggle (mở/thu) mục được click (chỉ với 1 lần click)
    void toggleItemExpansion(QTreeWidgetItem* item, int column);
    void updateStageActionsFromList(const QStringList& actionList);

private:
    QTreeWidget* treeWidget;  // Hiển thị công cụ theo TreeView
};

}  // namespace DockWnd
}  // namespace Gui

#endif  // GUI_STAGEVIEW_H

// NATAES Ngoc 2.2025