#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, messagebox, BOTTOM, Toplevel
from tkinter.ttk import Frame, Label, Entry, Combobox, Button
import sqlalchemy_data as db
from sqlalchemy_model import Evidence, Project


class ProjectSelector(Frame):

    def __init__(self, master):
        self.master = master
        self.master.title("Project-Selector")

        self.project_cmbx = None
        self.frame_header = Frame(self.master)
        self.frame_evidence = Frame(self.master)
        self.frame_footer = Frame(self.master)

        self.initUI()
        super().__init__()

    def initUI(self):

        first_column_width = 15

        frame1 = Frame(self.master)
        frame1.pack(fill=X)

        project_lbl = Label(frame1, text="Select Project", width=first_column_width)
        project_lbl.pack(side=LEFT, padx=5, pady=5)

        self.project_cmbx = Combobox(frame1)
        self.project_cmbx['values'] = [x.name for x in db.get_all_projects()]
        self.project_cmbx.bind('<<ComboboxSelected>>', self.project_selected)
        self.project_cmbx.pack(fill=X)

        self.frame_evidence.pack(fill=X)

        bttn_new_evidence = Button(self.frame_footer, text="New Evidence", command=self.click_new_evidence)
        bttn_new_evidence.pack(side=TOP, padx=5, pady=5)

        self.frame_footer.pack(side=BOTTOM)

    def project_selected(self, e):
        if self.project_cmbx.get():
            project = db.get_project_by_name(self.project_cmbx.get())
            print(project)

        self.frame_evidence.destroy()
        self.frame_evidence = Frame(self.master)
        self.frame_evidence.pack(fill=X)

        evidences = db.get_evidences_by_project_name(project.id)
        for evidence in evidences:
            evidence_lbl = Label(self.frame_evidence, text=evidence)
            evidence_lbl.pack(side=TOP)

    def click_new_evidence(self):
        self.ef = EvidenceWindow(Toplevel(self.master))


class EvidenceWindow(Frame):

    def __init__(self, master):
        self.master = master
        self.master.title("Evidence-Selector")

        self.project_cmbx = None
        self.frame_evidence = None
        self.frame_footer = None

        self.initUI()
        super().__init__()

    def initUI(self):
        # self.pack(fill=BOTH, expand=True)

        first_column_width = 15

        frame1 = Frame(self.master)
        frame1.pack(fill=X)


class Example(Frame):

    def __init__(self, message):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Review")
        self.pack(fill=BOTH, expand=True)

        first_column_width = 10

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Title", width=first_column_width)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Author", width=first_column_width)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=first_column_width)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


def main():
    root = Tk()
    root.geometry("300x300+300+300")
    app = ProjectSelector(root)
    root.mainloop()


if __name__ == '__main__':
    main()
