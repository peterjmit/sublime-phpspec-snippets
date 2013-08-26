import sublime
import sublime_plugin

class PhpspecExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    view.run_command("expand_selection", {"to": "line"})

    targets = []
    selections = view.sel()
    for selection in selections:
      # do replacement
      self.replace(edit, selection)
      # create new target for cursor movement
      targets.append(self.move_selection_down_two(selection))

    # Move the cursor to the new target(s)
    selections.clear()
    for target in targets:
      selections.add(target)

  # I have no idea how to do this properly...
  def move_selection_down_two(self, selection):
    view = self.view
    move_to_row, _ = view.rowcol(selection.end())
    # second argument here should be end of line,
    # not beginning (i.e. 0 is wrong)
    pt = view.text_point(move_to_row + 2, 0)

    return sublime.Region(pt)

  def replace(self, edit, selection):
    string = self.view.substr(selection)
    string = self.normalize_line_endings(string)

    if string == "" or string == "\n":
      return

    self.view.replace(edit, selection, self.string_to_example(string))

  # transforms string "should turn a string into a PhpSpec example" into
  # """
  # function it_should_turn_a_string_into_a_phpspec_example()
  # {
  #
  # }
  # """
  def string_to_example(self, string):
    has_newline = "\n" == string[-1]
    words = string.lower().strip().split(" ")

    if not words:
      return ""

    # remove function from beginning of the word list
    # it will get added later
    if words[0] == "function":
      words = words[1:]

    # add "it" to beginning of sentence if it doesnt exist
    first_word = words[0]
    if first_word != "it" and first_word != "its":
      words.insert(0, "it")

    return self.finish_string(words, has_newline)

  def normalize_line_endings(self, string):
    return string.replace('\r\n', '\n').replace('\r', '\n')

  # join the word list with "function" at the beginning, "()" at the end
  # and add {}. Add newline at the end if the string originally had one
  def finish_string(self, words, has_newline):
    string = "function " + "_".join(words) + "()"

    line_endings = self.view.settings().get('default_line_ending')
    if line_endings == 'windows':
      newline = "\r\n"
    elif line_endings == 'mac':
      newline = "\r"
    else:
      newline = "\n"

    # Probably not the right way to handle indentation
    string = newline.join(["\t" + string, "\t{", "\t\t", "\t}"])

    if has_newline:
        string = string + newline

    return string
