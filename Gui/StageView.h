// NATAES Ngoc 2.2025
// #ifndef GUI_STAGEVIEW_H
// #define GUI_STAGEVIEW_H

// #include <QDockWidget>
// #include <QTreeWidget>

// namespace Gui
// {
// namespace DockWnd
// {

// class StageView: public QDockWidget
// {
//     Q_OBJECT

// public:
//     explicit StageView(QWidget* parent = nullptr);
//     ~StageView() override;
//     // void updateStageActions();

// public Q_SLOTS:
//     // Slot để toggle (mở/thu) mục được click (chỉ với 1 lần click)
//     void toggleItemExpansion(QTreeWidgetItem* item, int column);
//     void updateStageActionsFromList(const QStringList& actionList);

// private:
//     QTreeWidget* treeWidget;  // Hiển thị công cụ theo TreeView
// };

// }  // namespace DockWnd
// }  // namespace Gui

// #endif  // GUI_STAGEVIEW_H
#ifndef STAGEVIEW_H
#define STAGEVIEW_H

#include <QDockWidget>
#include <QListWidget>
#include "Selection.h"
#include "App/DocumentObject.h"  // Định nghĩa App::DocumentObject
#include "App/Document.h"        // Định nghĩa App::Document

namespace Gui
{
namespace DockWnd
{

class StageView: public QDockWidget
{
    Q_OBJECT

public:
    StageView(QWidget* parent = nullptr);
    ~StageView() override;

private Q_SLOTS:
    void onItemClicked(QListWidgetItem* item);
    void onSelectionChanged(const Gui::SelectionChanges& msg);

private:
    void updateList();

    QListWidget* listWidget;
};

}  // namespace DockWnd
}  // namespace Gui

// Đăng ký App::DocumentObject* với Qt meta-object system
Q_DECLARE_METATYPE(App::DocumentObject*)

#endif  // STAGEVIEW_H

// NATAES Ngoc 2.2025