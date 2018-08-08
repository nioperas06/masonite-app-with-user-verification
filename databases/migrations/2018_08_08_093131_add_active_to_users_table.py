from orator.migrations import Migration


class AddActiveToUsersTable(Migration):

    def up(self):
        with self.schema.table('users') as table:
            table.boolean('active').default(False)

    def down(self):
        with self.schema.table('users') as table:
            table.drop_column('active')
